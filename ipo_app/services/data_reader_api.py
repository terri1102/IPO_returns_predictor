def price(name, start, end):
  from services.dart_api import dart
  corp_number = dart.find_corp_code(name)
  prices = web.DataReader(corp_number,'naver', start=start, end=end)
  price = prices['Close']
  return price