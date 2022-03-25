# sell2

if ( buy_vol[1] != 0 ) :
    if ( close > buy_price[1] * (1 + up1) or buy_num[1] >= num_limit1 ) :
        
        # buy_vol[1] 만큼 sell operation
        upbit.sell_market_order("KRW-BTG", buy_vol[1])

        count           = 0 

        buy_count[1]    = 0 
        buy_num[1]      = 0 
        buy_vol[1]      = 0

    else :
        
        buy_num[1] =  buy_num[1] + 1
