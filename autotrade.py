import time
import pyupbit
import datetime
import numpy as np


access = "BgyVpvO8MOEmDg7j1XocJq4xcrSWYoShtAvlteJ2"
secret = "zlYA1hl4Dxguqei2xRXEf2eDEglibSitxcu5oxun"


# 로그인
upbit = pyupbit.Upbit(access, secret)


# 파라미터 ( BTG 5minute )

buy_count   = np.array([0, 0, 0]) 
buy_vol     = np.array([0, 0, 0]) 
buy_price   = np.array([0, 0, 0]) 
buy_num     = np.array([0, 0, 0])

count       = 0 


up0         = 0.53/ 100 
up1         = 0.90/100 
up2         = 0.51/100 
num_limit0  = 1.7* 60 /5  
num_limit1  = 1.94* 60 /5 
num_limit2  =  3* 60 /5 

tic_perc    = 0.031 / 100

n_count     = 4
bigone      = 9.41
tic_init    = -0.4


# time check 초기화
OHLCV_temp  = pyupbit.get_ohlcv(ticker="KRW-BTG", interval='minute5', count=2, to=None, period=0.1)
time_prev   = np.array( [OHLCV_temp.index[0], OHLCV_temp.index[1]] ) # [0] : 과거, [1] : 최근

# autotrade start
while True:
    
    time.sleep(3)
    print(count)
    try :

        OHLCV_temp  = pyupbit.get_ohlcv(ticker='KRW-BTG', interval='minute5', count=2, to=None, period=0.1)
        time_new    = np.array( [OHLCV_temp.index[0], OHLCV_temp.index[1]] )


        if ( time_prev[0] != time_new[0] ) :

            # get open, close, delta
            time_prev   = time_new
            OHLCV       = OHLCV_temp.to_numpy()
            open        = OHLCV[0,0]
            close       = OHLCV[0,3]
            delta       = close - open
                
            # get tic
            tic         =  open * tic_perc 

            # count tic number
            if ( delta < - tic ) :
                count       = count + 1 
                
            elif delta > tic * tic_init :
                count       = 0 

 

            # buy
            if   ( np.sum(buy_count) == 0) :
                if ( count >= n_count ) or ( delta < -tic * bigone ) :
                    # get balance
                    balance     = upbit.get_balance("KRW")

                    # 10% buy operation
                    upbit.buy_market_order("KRW-BTG", balance * 0.1)
                    buy_price[0]    = pyupbit.get_current_price("KRW-BTG")
                    buy_vol[0]      = balance * 0.1 / pyupbit.get_current_price("KRW-BTG")
                    buy_count[0]    = 1 
                    buy_num[0]      = 1 

                    count           = 0 

            elif (np.sum(buy_count) == 1) :
                temp            = np.where(buy_count == 0)
                temp2           = np.asarray(temp)
                new             = temp2[0,0]

                if ( count >= n_count ) or ( delta < -tic * bigone ) :
                    # get balance
                    balance     = upbit.get_balance("KRW")
                    
                    # 90% buy operation
                    upbit.buy_market_order("KRW-BTG", balance * 0.9)
                    buy_price[new]      = pyupbit.get_current_price("KRW-BTG")
                    buy_vol[new]        = balance * 0.9 / pyupbit.get_current_price("KRW-BTG")
                    buy_count[new]      = 1 
                    buy_num[new]        = 1 
                    
                    count               = 0 

            elif (np.sum(buy_count) == 2) :
                temp            = np.where(buy_count == 0)
                temp2           = np.asarray(temp)
                new             = temp2[0,0]

                if ( count >= n_count ) or ( delta < -tic * bigone ) :
                    # get balance
                    balance     = upbit.get_balance("KRW")

                    # 100% buy operation
                    upbit.buy_market_order("KRW-BTG", balance* 99.8/100)
                    buy_price[new]      = pyupbit.get_current_price("KRW-BTG")
                    buy_vol[new]        = balance* 99.8/100 /pyupbit.get_current_price("KRW-BTG")
                    buy_count[new]      = 1 
                    buy_num[new]        = 1 

                    count               = 0 

            # sell

            if ( buy_vol[0] != 0 ) :
                if ( close > buy_price[0] * (1 + up0) or buy_num[0] >= num_limit0 ) :
                    
                    # buy_vol[0] 만큼 sell operation
                    upbit.sell_market_order("KRW-BTG", buy_vol[0]*0.999)
                    
                    count           = 0 

                    buy_count[0]    = 0 
                    buy_num[0]      = 0 
                    buy_vol[0]      = 0
                    
                else :
                    
                    buy_num[0] =  buy_num[0] + 1 
                        

            if ( buy_vol[1] != 0 ) :
                if ( close > buy_price[1] * (1 + up1) or buy_num[1] >= num_limit1 ) :
                    
                    # buy_vol[1] 만큼 sell operation
                    upbit.sell_market_order("KRW-BTG", buy_vol[1]*0.999)

                    count           = 0 

                    buy_count[1]    = 0 
                    buy_num[1]      = 0 
                    buy_vol[1]      = 0

                else :
                    
                    buy_num[1] =  buy_num[1] + 1


        
            if ( buy_vol[2] != 0 ) :
                if ( close > buy_price[2] * (1 + up2) or buy_num[2] >= num_limit2 ) :
                    
                    # buy_vol[2] 만큼 sell operation
                    upbit.sell_market_order("KRW-BTG", buy_vol[2]*0.999)

                    count           = 0 

                    buy_count[2]    = 0 
                    buy_num[2]      = 0 
                    buy_vol[2]      = 0
    

                else :
                    
                    buy_num[2] =  buy_num[2] + 1


    except :
        print("error!")
        time.sleep(3) # n 초 동안 작동 안함
        
