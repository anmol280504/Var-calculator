import csv

def read_csv_data(filename):
    dict1 = {}
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)  
            for row in reader:
                probability = float(row["Probability"])
                loss = float(row["Loss"])
                dict1[loss] = probability
    except FileNotFoundError:
        print("Error: File" + filename + " not found.")
    except KeyError as e:
        print("Error: Missing expected column" + e + " in the file.")
    return dict1

def calculate_var(dataDict, confidence_level):
    loss = []
    for i in dataDict:
        loss.append(i)
   
    loss.sort()

    cumulative_probability = 0.0
    psbleans = []
    for losses in loss:
        probability = dataDict[losses]
        cumulative_probability += probability
        if cumulative_probability >= (confidence_level):
             psbleans.append(losses)

    psbleans.sort()
    print(psbleans)
    return psbleans[0]


def main():
    filename = "data.csv"  
    confidence_level = input("Enter confidence level (0-1): ")
    if(float(confidence_level) > 1.0 or float(confidence_level) < 0.0):
        print("Incorrect confindence level.")
        return
    data = read_csv_data(filename)
    if not data:
        return 
 
    var = calculate_var(data, float(confidence_level))
    print(f"Value at Risk (VaR) at {float(confidence_level) * 100}% confidence level is: ${abs(var)}")

main()

