#|-----------------------------------------------------------------|
#| This is an app I'm working on to automate quickly graphing data |
#|-----------------------------------------------------------------|

def df_graph(data):
    import pandas as pd
    import matplotlib as mpl
    from matplotlib import pyplot as plt

    pd.options.display.mpl_style = 'default'

    df = pd.read_csv(data)
    print df.columns
    print '\n'
    print 'Please choose from these columns from your data to specify x and y parameters for your graph'
    x = raw_input('x-param: ')
    y = raw_input('y-param: ')
    print 'What type of graph would you like to create?'
    kind = raw_input('graph-type: ')
    
    print 'Make sure data is up to date!'
    print '\n'
        #print 'Please provide number of days you would like to graph'
        #first_daysago = int(raw_input('How many days ago do you want begin the graph: '))
        #last_daysago = int(raw_input('How many days ago would you like the end the graph: '))
        #start = (len(df.columns[0])-first_daysago)
        #end = (len(df.columns[0])-last_daysago)

        #df.plot(kind='line', x=x, y=y, xlim=(start,end), figsize=(20,15))
    df.plot(kind=kind, x=x, y=y, figsize=(20,15), legend=True)
    
        #if bar graph: xlim = -0.5,max+.5
