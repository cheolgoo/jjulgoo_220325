# sell1

if ( buy_vol[0] != 0 ) :
    if ( close > buy_price[0] * (1 + up0) or buy_num[0] >= num_limit0 ) :
        
        # buy_vol[0] 만큼 sell operation
        upbit.sell_market_order("KRW-BTG", buy_vol[0])
        
        count           = 0 

        buy_count[0]    = 0 
        buy_num[0]      = 0 
        buy_vol[0]      = 0
        
    else :
        
        buy_num[0] =  buy_num[0] + 1 
        
