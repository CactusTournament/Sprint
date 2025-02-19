# Description: Newfoundland Chocolate Company Employee Travel Claim
# Author: Cameron Boyer
# Date(s): February 17, 2025 - February 26, 2025


# Define required libraries.
import datetime


# Define program constants.
DATE_BONUS1 = datetime.datetime(2025, 12, 15)
DATE_BONUS2 = datetime.datetime(2025, 12, 22)

PER_DIEM = 85.00
MILE_AMOUNT_RENTAL = 65.00
BONUS_DATE = 50.00
EXEC_BONUS = 45.00
DAY_BONUS = 100.00


MILE_AMOUNT_RATE = .17
HST_RATE = .15
KM_BONUS_RATE = .04

# Main program starts here.
while True:
    
    
    # Gather user inputs.
    while True:
        EmployeeNum = input("Please enter employee number (XXXXX): ")
        if EmployeeNum != "" and len(EmployeeNum) == 5:
            break
        else:
            print()
            print("Error - Employee number must be entered and contain five characters.")
            print()
        
    while True:
        EmployeeNameFirst = input("Please enter employee first name: ").title()
        if EmployeeNameFirst != "":
            break
        else:
            print()
            print("Error - Employee first name must be entered.")
            print()
    while True:
        EmployeeNameLast = input("Please enter employee last name: ").title()
        if EmployeeNameLast != "":
            break
        else:
            print()
            print("Error - Employee last name must be entered.")
            print()
    while True:
        EmployeeLoc = input("Please enter trip location: ").title()
        if EmployeeLoc != "":
            break
        else:
            print()
            print("Error - Trip location must be entered.")
            print()
    while True:
        try:
            StartDate = input("Please enter start date (YYYY-MM-DD): ")
            StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
        except:
            print()
            print("Error - Start date must be entered and in the format YYYY-MM-DD.")
            print()
        else:
            break
    while True:
        try:
            EndDate = input("Please enter end date (YYYY-MM-DD): ")
            EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
            Days = (EndDate - StartDate).days
        except:
            print()
            print("Error - End date must be entered and in the format YYYY-MM-DD.")
            print()
        else:
            if EndDate < StartDate:
                print()
                print("Error - End date must be after start date.")
                print()
            elif Days > 7:
                print()
                print("Error - Trip must be 7 days or less.")
                print()
            else:
                break
    while True:
        CarUsed = input("Do you own or did you rent the car used? (O/R): ").upper()
        if CarUsed == "O" or CarUsed == "R":
            break
        else:
            print()
            print("Error - Please enter O or R only.")
            print()
    while True:
        if CarUsed == "O":
            TotKm = input("Please enter the number of kilometers traveled: ")
            if TotKm == "":
                print()
                print("Error - Kilometers must be entered.")
                print()
            else:
                TotKm = int(TotKm)
                if TotKm > 2000:
                    print()
                    print("Error - Kilometers cannot exceed 2000.")
                    print()
                else:
                    if TotKm > 1000:
                        BonusKm = KM_BONUS_RATE * TotKm
                    break
        else:
            break
    while True:
        ClaimType = input("Is this a Stardard or an Executive claim? (S/E): ").upper()
        if ClaimType == "S" or ClaimType == "E":
            break
        else:
            print()
            print("Error - Please enter S or E only.")
            print()
    
    
    # Perform required calculations.

    PerDiemAmt = PER_DIEM * Days
    
    if CarUsed == "O":
        MileAmt = MILE_AMOUNT_RATE * TotKm
    else:
        MileAmt = MILE_AMOUNT_RENTAL * Days

    if Days > 3:
        BonusDays = DAY_BONUS
    else:
        BonusDays = 0.00

    if ClaimType == "E":
        BonusExec = EXEC_BONUS * Days
    else:
        BonusExec = 0.00

    if DATE_BONUS1 <= StartDate <= DATE_BONUS2:
        BonusDate = BONUS_DATE * Days
    else:
        BonusDate = 0.00
    
    TotBonus = BonusDays + BonusKm + BonusExec + BonusDate

    ClaimAmt = PerDiemAmt + MileAmt + TotBonus
    Hst = HST_RATE * ClaimAmt
    TotClaim = ClaimAmt + Hst

    StartDateDsp = datetime.datetime.strftime(StartDate, "%Y-%m-%d")
    EndDateDsp   = datetime.datetime.strftime(EndDate, "%Y-%m-%d")
    EmployeeName = EmployeeNameFirst + " " + EmployeeNameLast
    CarUsedDsp    = "Owned" if CarUsed == "O" else "Rented"
    ClaimTypeDsp  = "Standard" if ClaimType == "S" else "Executive"
    PerDiemAmtDsp = "${:.2f}".format(PerDiemAmt)
    MileAmtDsp    = "${:.2f}".format(MileAmt)
    BonusDaysDsp = "${:,.2f}".format(BonusDays)
    BonusExecDsp = "${:,.2f}".format(BonusExec)
    BonusDateDsp = "${:,.2f}".format(BonusDate)
    TotBonusDsp  = "${:,.2f}".format(TotBonus)
    ClaimAmtDsp = "${:,.2f}".format(ClaimAmt)
    HstDsp      = "${:.2f}".format(Hst)
    TotClaimDsp = "${:,.2f}".format(TotClaim)


    # Display results

    print()
    print(f"Newfoundland Chocolate Company            Start Date:  {StartDateDsp:<10s}")
    print(f"Employee Travel Claim                     End Date:    {EndDateDsp:<10s}")
    print(f"------------------------------            -----------------------")
    print(f"Employee Name:   {EmployeeName:<24s} Employee Number:  {EmployeeNum:<5s}")
    print(f"Claim Type:      {ClaimTypeDsp:<10s}               -----------------------")
    print(f"Trip Location:   {EmployeeLoc:<24s} Total Days:          {Days:>2d}")
    print(f"Car Used:        {CarUsedDsp:<10s}               -----------------------")
    print()
    print(f"-----------------------------------------------------------------")
    if CarUsed == "O":
        print(f"Total Kilometers:       {TotKm:>4d}km")
    print()
    print(f"Day Bonus:          {BonusDaysDsp:>10s}            Mileage:     {MileAmtDsp:>10s}")
    print(f"Executive Bonus:    {BonusExecDsp:>10s}            Per Diem:    {PerDiemAmtDsp:>10s}")
    print(f"Total Bonus:        {TotBonusDsp:>10s}            Date Bonus:  {BonusDateDsp:>10s}")
    print(f"-----------------------------------------------------------------")
    print(f"Total Claim:        {ClaimAmtDsp:>10s}            HST:         {HstDsp:>10s}")
    print(f"-----------------------------------------------------------------")
    print(f"Total Claim Amount: {TotClaimDsp:>10s}")
    print(f"-----------------------------------------------------------------")
    print()
    print(f"  Thank you for your submission. Your claim has been processed!")
    print()
    Continue = input("       Would you like to enter another claim? (Y/N): ").upper()
    if Continue == "N":
        print("Exiting the program... Have a good day!")
        break
    


    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.