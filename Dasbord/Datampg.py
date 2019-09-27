import pandas as pd

def data_mpg():
    df = pd.read_csv('clean.csv')
    return df

def Data_horsepower():
    df = pd.read_csv('clean.csv')
    horsepower_usa=list(df[df['origin']=='usa'].sort_values(['horsepower'],ascending=False)['name'].head(3).values)
    horsepower_japan=list(df[df['origin']=='japan'].sort_values(['horsepower'],ascending=False)['name'].head(3).values)
    horsepower_europe=list(df[df['origin']=='europe'].sort_values(['horsepower'],ascending=False)['name'].head(3).values)
    Rank=[]
    for i in range(len(horsepower_usa)):
        r=i+1
        Rank.append('Rank '+str(r))
    Rank
    dictrankhorsepower= {
        'Ranking' : Rank,
        'usa' : horsepower_usa,
        'japan' : horsepower_japan,
        'europe' : horsepower_europe,
    }
    horsepower_rank=pd.DataFrame(dictrankhorsepower)
    horsepower_rank=horsepower_rank.set_index([Rank])
    return horsepower_rank

def Data_irit():
    df = pd.read_csv('clean.csv')
    mpg_usa=list(df[df['origin']=='usa'].sort_values(['mpg'],ascending=False)['name'].head(3).values)
    mpg_japan=list(df[df['origin']=='japan'].sort_values(['mpg'],ascending=False)['name'].head(3).values)
    mpg_europe=list(df[df['origin']=='europe'].sort_values(['mpg'],ascending=False)['name'].head(3).values)
    Rank=[]
    for i in range(len(mpg_usa)):
        r=i+1
        Rank.append('Rank '+str(r))
    Rank
    dictrankmpg= {
        'Ranking' : Rank,
        'usa' : mpg_usa,
        'japan' : mpg_japan,
        'europe' : mpg_europe,
    }
    mpg_rank=pd.DataFrame(dictrankmpg)
    mpg_rank=mpg_rank.set_index([Rank])
    return mpg_rank