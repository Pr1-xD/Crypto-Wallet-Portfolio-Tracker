from moralis import evm_api
import time

api_key = "TL5rt69l60RFyJV97j88BloPRLvnNHt2c9NCDb2f3TMqOYfu6IdKmtdJmBrJUjVb"

address="0xb4C87e51eF9f3D978a6025Eb1fC0869cc65E878F"

def getPrice(address):
  params = {
  "chain": "eth",
  "exchange": "uniswap-v2",
  "address": address
}
  result = evm_api.token.get_token_price(
  api_key=api_key,
  params=params,
)
  return result

def getPortfolioValue(balance):
    totalValue=0
    for x in balance:
        
        if x['possible_spam']:
            # print('Found spam token')
            continue
        else:
            try:
                price = getPrice(x["token_address"])
            except:
                continue    
            else:    
                # print(price['usdPrice'])
                # print(float(x['balance'])/10**18)
                value = (float(x['balance'])/10**x['decimals']) * price['usdPrice']
                # print(value)
                totalValue = totalValue + value
    return totalValue 


params = {
  "chain": "eth",
  "token_addresses": [],
  "address": address
}

balancePresent = evm_api.token.get_wallet_token_balances(
  api_key=api_key,
  params=params,
)

presentValue = getPortfolioValue(balancePresent)
print("Present",presentValue)
# print(int(time.time()))
# print(int(time.time())-86400)

########################
########################
#       1 Day          # 
########################
########################

params = {
  "chain": "eth",
  "date": str(int(time.time())-86400)
}

oneDayBlock = evm_api.block.get_date_to_block(
  api_key=api_key,
  params=params,
)

params = {
  "chain": "eth",
  "to_block": oneDayBlock['block'],
  "token_addresses": [],
  "address": address
}

balanceOneDay = evm_api.token.get_wallet_token_balances(
  api_key=api_key,
  params=params,
)

oneDayValue = getPortfolioValue(balanceOneDay)
print("1 Day Balance",oneDayValue)
print("1 Day PNL",presentValue-oneDayValue)


########################
########################
#       7 Day          # 
########################
########################


params = {
  "chain": "eth",
  "date": str(int(time.time())-(86400*7))
}

sevenDayBlock = evm_api.block.get_date_to_block(
  api_key=api_key,
  params=params,
)

params = {
  "chain": "eth",
  "to_block": sevenDayBlock['block'],
  "token_addresses": [],
  "address": address
}

balanceSevenDay = evm_api.token.get_wallet_token_balances(
  api_key=api_key,
  params=params,
)

sevenDayValue = getPortfolioValue(balanceSevenDay)
print("7 Day Balance",sevenDayValue)
print("7 Day PNL",presentValue-sevenDayValue)

########################
########################
#       30 Day         # 
########################
########################


params = {
  "chain": "eth",
  "date": str(int(time.time())-(86400*30))
}

thirtyDayBlock = evm_api.block.get_date_to_block(
  api_key=api_key,
  params=params,
)

params = {
  "chain": "eth",
  "to_block": thirtyDayBlock['block'],
  "token_addresses": [],
  "address": address
}

balanceThirtyDay = evm_api.token.get_wallet_token_balances(
  api_key=api_key,
  params=params,
)

thirtyDayValue = getPortfolioValue(balanceThirtyDay)
print("30 Day Balance",thirtyDayValue)
print("30 Day PNL",presentValue-thirtyDayValue)
