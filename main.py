import pandas as pd
import glob
import os

def read_json():
    df = pd.read_json('CV1.json')
    df['start_time'] = pd.to_timedelta(df['s'], unit='ms')
    df['end_time'] = pd.to_timedelta(df['e'], unit='ms')

    df.resample('start_time').sum()

def read_srt(path):
    print('PATH')
    print(path)
    input()
    with open(path) as f:
        lines = f.readlines()
        print(lines)
    ts = []
    texts = []
    data = []
    for line in lines:
        if len(line) < 3:
            print('skipping')
            print(line)

        if line.startswith('00:') or line.startswith('01:'):
            ts.append(line.strip())
            
            texts.append(' '.join(data))
            data = []

        else:
            data.append(line.strip())
    dff = pd.DataFrame({'TimeStamp': ts, 'Text': texts}) 
    fn = os.path.basename(path)
    #print(fn)
    #input()
    
    dff['Text'] = dff['Text'].apply(lambda x: x.split('  ')[0])
    dff.to_csv(os.path.join('csv', fn + '.csv')  ) 
    return dff
    #return ts, texts



def main():
    src_path = 'srt'
    for f in glob.glob(os.path.join(src_path, '*.srt')):
        print(f)
        input()
        read_srt(f)


if __name__ == '__main__':
    main()
