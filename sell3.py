# sell3

if ( buy_vol[2] != 0 ) :
    if ( close > buy_price[2] * (1 + up2) or buy_num[2] >= num_limit2 ) :
        
        # buy_vol[2] 만큼 sell operation
        upbit.sell_market_order("KRW-BTG", buy_vol[2])

        count           = 0 

        buy_count[2]    = 0 
        buy_num[2]      = 0 
        buy_vol[2]      = 0
        

    else :
        
        buy_num[2] =  buy_num[2] + 1
        
