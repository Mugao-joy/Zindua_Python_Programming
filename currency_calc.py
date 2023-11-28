#currency converter app 
#Input Handling: The app prompts the user to input the amount to convert and the source and target currencies.
while True:
    exchange_rates = {
    'JPY' : 110,
    'GBP' : 10,
    'EUR' : 8,
    'KSH' : 152,
}

    print('Welcome! You can now convert JPY, GBP, EUR and KSH')

    source_currency = input(' Please enter the source currency you want to convert (JPY,GBP,EUR or KSH): ').upper()
    if source_currency not in exchange_rates:
        print('Invalid. You can only convert JPY, GBP, EUR and KSH.')
        source_currency = input(' Please enter the source currency you want to convert (JPY,GBP,EUR or KSH): ').upper()


    target_currency = input('Please enter the currency to convert to (JPY,GBP,EUR or KSH): ').upper()
    if target_currency not in exchange_rates:
        print('Invalid. You can only convert JPY, GBP, EUR and KSH.')
        target_currency = input('Please enter the currency to convert to (JPY,GBP,EUR or KSH): ').upper()

    if source_currency == target_currency:
        print('Please Try again')
        quit()

    amount = float(input('Please enter the amount you want to convert: '))

    exchange_rate_source = exchange_rates[source_currency]
    exchange_rate_target = exchange_rates[target_currency]
    converted_amount = amount * (exchange_rate_target / exchange_rate_source)


    print('Original amount:', amount, source_currency)
    print('Converted amount: ',converted_amount, target_currency)

    another_conversion = input('Do you want to perform another conversion?(yes/no): ').lower()
    if another_conversion != 'yes':
        quit()
