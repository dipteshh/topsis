import pandas as pd
import numpy as np
import sys

class IncompleteValues(Exception):
    pass

class ImpactError(Exception):
    pass

class ParametersError(Exception):
    pass

class CommaError(Exception):
    pass

class NegativeWeightsError(Exception):
    pass

class LessColumnsError(Exception):
    pass

class DataTypeError(Exception):
    pass


def main () :
    try:
        if len(sys.argv) != 5 :
            raise ParametersError
        data = sys.argv[1]
        weights = sys.argv[2]
        impacts = sys.argv[3]
        result_filename = sys.argv[4]
        data = pd.read_excel(data)
        print(data)

        names = data.iloc[:,0]
        data = data.iloc[:,1:]

        #error checking
        if data.shape[1]<2 :
            raise LessColumnsError
        for i in range(data.shape[1]):
            if data.iloc[:, i].dtype.kind not in 'iufc':
                raise DataTypeError
        if (',' not in weights) or (',' not in impacts):
            raise CommaError
        weights = weights.split(',')
        impacts = impacts.split(',')
        if (len(weights) != data.shape[1]) or (len(impacts) != data.shape[1]):
            raise IncompleteValues
        for i in impacts:
            if i == '+' or i == '-':
                continue
            else:
                raise ImpactError

        for i in range(len(weights)):
            weights[i] = float(weights[i])
            if i < 0:
                raise NegativeWeightsError

        norm_data = data/np.linalg.norm(data,axis=0)
        print(norm_data)

        weighted_data = norm_data * weights
        print(weighted_data)

        ideal_best = []
        ideal_worst = []
        for j in range(len(data.columns)) :
            imp = impacts[j]
            if imp == "+" :
                ideal_best.append(weighted_data.iloc[:,j].max())
                ideal_worst.append(weighted_data.iloc[:,j].min())
            else :
                ideal_best.append(weighted_data.iloc[:,j].min())
                ideal_worst.append(weighted_data.iloc[:,j].max())
        print(ideal_best)
        print(ideal_worst)

        dist_pos = np.sqrt(np.sum((weighted_data - ideal_best)**2,axis = 1))
        dist_neg = np.sqrt(np.sum((weighted_data - ideal_worst)**2,axis = 1))
        print(dist_pos)
        print(dist_neg)

        p_score = dist_neg/(dist_pos + dist_neg)
        print(p_score)

        rankings = np.argsort(p_score)
        print("Rankings : ")
        print(rankings)
        data['Name'] = names
        data['Score'] = p_score
        data['Rank'] = rankings
        data.to_csv(result_filename,index=False)
    
    except FileNotFoundError:
        print("Input File not found ")
    except ParametersError:
        print("Incorrect number of parameters ")
    except LessColumnsError:
        print("Less than 3 columns are there ")
    except DataTypeError:
        print("Incorrect data type found ")
    except CommaError:
        print("Enter weights and impacts correctly using ',' ")
    except IncompleteValues:
        print("Wrong inputs for weights or impacts ")
    except ImpactError:
        print("Enter only '+' or '-' for impacts ")
    except NegativeWeightsError:
        print("Weights should be +ve")



main()