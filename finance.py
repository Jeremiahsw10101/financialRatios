import locale
locale.setlocale(locale.LC_ALL, '')

class Finance:
    def __init__(self):
        pass

    def weighted_avg_cost_cap(self):
        print("\n******WACC Calculator******\n")
        try:
            Re = float(input("Cost of equity: ")) / 100
            Rd = float(input("Cost of debt: ")) / 100
            E = float(input("Market value of the firm's equity: "))
            D = float(input("Market value of the firm's debt: "))
            Tc = float(input("Corporate tax rate: ")) / 100
        except ValueError:
            print("Invalid input")
            return

        V = E + D
        equityPercentage = E / V
        debtPercentage = D / V
        wacc = ((equityPercentage * Re) + (debtPercentage * Rd * (1 - Tc))) * 100
        print(f"The weighted average cost of capital is {wacc:.2f}%")

    def enterprise_value(self):
        print("\n******Enterprise Value Calculator******\n")
        try:
            StkPrice = float(input("Current stock price: "))
            SO = int(input("Shares outstanding: "))
            TD = float(input("Total debt: "))
            TC = float(input("Total cash: "))
        except ValueError:
            print("Invalid input")
            return

        MktCap = StkPrice * SO
        EV = MktCap + TD - TC
        formatted_EV = locale.currency(EV, grouping=True)
        print(f"The enterprise value of the firm is {formatted_EV}")

    def return_on_inv(self):
        try:
            gain = float(input("Gain from investment: "))
            cost = float(input("Cost of investment: "))
        except ValueError:
            print("Invalid input")
            return

        ROI = (gain - cost) / cost * 100
        print(f"The return on investment is {ROI:.2f}%")

    def liquidity_ratios(self):
        try:
            CA = float(input("Current assets: "))
            CL = float(input("Current liabilities: "))
            Inventory = float(input("Inventory: "))
        except ValueError:
            print("Invalid input")
            return

        currentRatio = CA / CL
        quickRatio = (CA - Inventory) / CL
        workingCap = CA - CL
        formatted_workingCap = locale.currency(workingCap, grouping=True)
        print(f"\nThe current ratio is {currentRatio:.2f}")
        print(f"\nThe quick ratio is {quickRatio:.2f}")
        print(f"\nThe firm's working capital is {formatted_workingCap}")

    def financial_leverage_ratios(self):
        try:
            TD = float(input("Total debt: "))
            TA = float(input("Total assets: "))
            TE = float(input("Total equity: "))
            EBIT = float(input("EBIT: "))
            IntExp = float(input("Interest expense: "))
        except ValueError:
            print("Invalid input")
            return

        DebtRatio = TD / TA
        D2ERatio = TD / TE
        IntCoverageRatio = EBIT / IntExp
        print(f"\nThe debt ratio is {DebtRatio:.2f}")
        print(f"\nThe debt to equity ratio is {D2ERatio:.2f}")
        print(f"\nThe interest coverage ratio is {IntCoverageRatio:.2f}")

    def profitability_ratios(self):
        try:
            sales = float(input("Sales: "))
            COGS = float(input("Cost of goods sold: "))
            NI = float(input("Net income: "))
            TA = float(input("Total assets: "))
            SE = float(input("Shareholder Equity: "))
        except ValueError:
            print("Invalid input")
            return

        GPM = (sales - COGS) / sales
        ROA = NI / TA
        ROE = NI / SE
        print(f"\nThe firm's gross profit margin is {GPM:.2f}")
        print(f"\nThe firm's return on assets is {ROA:.2f}")
        print(f"\nThe firm's return on equity is {ROE:.2f}")

    def dividend_ratios(self):
        try:
            DPS = float(input("Dividends per share: "))
            SP = float(input("Share price: "))
            EPS = float(input("Earnings per share: "))
        except ValueError:
            print("Invalid input")
            return

        DY = DPS / SP * 100
        DPR = DPS / EPS * 100
        print(f"\nThe firm's dividend yield is {DY:.2f}%")
        print(f"\nThe firm's dividend payout ratio is {DPR:.2f}%")

companyX = Finance()
companyX.weighted_avg_cost_cap()
companyX.enterprise_value()
companyX.return_on_inv()
companyX.liquidity_ratios()
companyX.financial_leverage_ratios()
companyX.profitability_ratios()
companyX.dividend_ratios()
