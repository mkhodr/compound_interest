    
def compound_interest(value, interest, months, input=0):
    initial_value = value
    total_input = 0
    total_dividend_value = 0
    total_dividend_input = 0
    for i in range(months):
        # value inicial
        dividend_value = value * interest
        value += dividend_value
        total_dividend_value += dividend_value
        # Inputs
        dividend_input = (total_input + total_dividend_input) * interest
        total_input += input
        total_dividend_input += dividend_input
        # Total
    inputs = total_dividend_input + total_input
    total = value + inputs
    # print(f'{i+1} months | interest: {interest*100} a.m. | value inicial: {initial_value} | inputs mensais: {input}')
    # print(f'value final: {total:.2f} | Total aportado: {total_input:.2f} | value-input: {total-total_input} ')
    # print(f'Total dividend: {total_dividend_input+total_dividend_value:.2f} | Dividend value: {total_dividend_value:.2f} | Dividend input: {total_dividend_input:.2f}')
    return [[total, total_dividend_input+total_dividend_value],[input, total_dividend_input]]


