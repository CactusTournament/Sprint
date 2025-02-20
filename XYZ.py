# Description: XYZ Company is setting up a maintenance schedule for major pieces of equipment. 
# Author: Brandon Maloney & Group 6/SD 14
# Date(s): February 18, 2025 - Febuary 18, 2025


# Define required libraries.
import datetime
import os

# Define program constants.
CUR_DATE = datetime.datetime.now()

CLEANING_RATE = 10
TUB_FLUID_RATE = 21
MAJ_INSP_RATE = 180
SAL_PRICE_RATE = .1

# Define program functions.



# Main program starts here.
while True:
    
    # Gather user inputs.
    AllowedNum = set("0123456789")
    
    while True:
        EquipCost = input("Enter the equipment purchase total cost: ")
        if EquipCost == "":
            print()
            print("     Error - Purchase total cost must not be blank or <0.")
            print()
        elif set(EquipCost).issubset(AllowedNum) == False:
            print()
            print("     Error - Purchase total cost must be numeric only.")
            print()
        else:
            break
    EquipCost = float(EquipCost)
    while True:
        PurDate = input("Enter the equipment purchase date(YYYY-MM-DD): ")
        try:
            PurDate = datetime.datetime.strptime(PurDate, "%Y-%m-%d")
        except ValueError:
            print()
            print("     Error - Date is invalid. Use (YYY-MM-DD) format.")
            print()
            continue
        if PurDate > CUR_DATE:
            print()
            print("     Error - Purchase date cannot be in the future.")
            print()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            break
            

        # Perform required calculations.
    SalVal = EquipCost * SAL_PRICE_RATE
    Years = 15
    Months = Years * 12
    Days = Years * 365
    Amortization = (EquipCost - SalVal) / (Months)

    # Display results
    print(f"\n                 XYZ's Maintenance Schedule")
    print(f"                 ------------------------------     ")
    EquipCostDsp = "${:,.2f}".format(EquipCost)
    print(f"            Purchase Date:                {PurDate.strftime('%Y-%m-%d')}")
    print(f"            Equipment Cost:               {EquipCostDsp:<13s}")
    print(f"            Salvage Value:                ${SalVal:,.2f}")
    print(f"            Monthly Amortization:         ${Amortization:,.2f}")
    print()

    # Display maintenance schedule for each year
    print(f"  {'Year':<5} {'Day':<5}  {'Basic Clean':<12}    {'Tube/Fluid Check':<17}   {'Major Inspection':<17}")
    print(f"-----------------------------------------------------------------------")
    for day in range(1, Days + 1):
        CurrentDate = PurDate + datetime.timedelta(days=day)
        day_of_year = (CurrentDate - datetime.datetime(CurrentDate.year, 1, 1)).days + 1
        
        # Only calculate BasicClean if day is a multiple of CLEANING_RATE
        if day % CLEANING_RATE == 0:
            BasicCleanFormatted = CurrentDate.strftime("%Y-%m-%d")
        else:
            BasicCleanFormatted = ""

        # Only calculate TubeFluidChk if day is a multiple of TUB_FLUID_RATE
        if day % TUB_FLUID_RATE == 0:
            TubeFluidChkFormatted = CurrentDate.strftime("%Y-%m-%d")
        else:
            TubeFluidChkFormatted = ""

        # Only calculate MajorInsp if day is a multiple of MAJ_INSP_RATE
        if day % MAJ_INSP_RATE == 0:
            MajorInspFormatted = CurrentDate.strftime("%Y-%m-%d")
        else:
            MajorInspFormatted = ""
        
        # Only print the row if at least one of the dates is not empty
        
        if BasicCleanFormatted or TubeFluidChkFormatted or MajorInspFormatted:
            year = (day // 365) + 1
            print(f"   {year:<2}   {day_of_year:<3}    {BasicCleanFormatted:<11}     {TubeFluidChkFormatted:<11}         {MajorInspFormatted:<11}")

    print(f"-----------------------------------------------------------------------")
    print(f"| Invoice Date: {CUR_DATE.strftime('%Y-%m-%d')}                                            |")
    print(f"-----------------------------------------------------------------------")

    while True:
        if input("Would you like to enter another equipment purchase? (Y/N): ").upper() == "Y":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            exit()

    # Write the values to a data file for storage.


#yabadabadoo
# Any housekeeping duties at the end of the program.