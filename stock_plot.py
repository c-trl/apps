def stock_plot(share):
    from yahoo_finance import Share
    from pprint import pprint
    import pandas as pd
    from datetime import date, datetime, timedelta
    
    stock = Share(str(share))
    
    df = pd.DataFrame(stock.get_historical(str(date.today() - timedelta(days=730)), str(date.today())))
    
    df['Adj_Close'] = [float(x) for x in df['Adj_Close']]
    df['Close'] = [float(x) for x in df['Close']]
    df['High'] = [float(x) for x in df['High']]
    df['Low'] = [float(x) for x in df['Low']]
    df['Open'] = [float(x) for x in df['Open']]
    df['Date'] = [pd.to_datetime(x) for x in df['Date']]
    
    df.ix[:,[0,1,2,3,4,5]].plot(figsize=(20,5), 
                                x='Date', 
                                title=str(share)+ ' Stock Information, ' + str(date.today() - timedelta(days=730))+' - '+ str(date.today()))
