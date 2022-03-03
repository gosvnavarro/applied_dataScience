# Question 1
def proportion_of_education():
    import pandas as pd
    import numpy as np

    df = pd.read_csv("assets/NISPUF17.csv", index_col = 0)
    
    EDUS = df['EDUC1']
    edus = np.sort(EDUS.values)
    
    count_POE = {"less than high school": 0, 
                 "high school": 0, 
                 "more than high school but not college": 0, 
                 "college": 0}
    n = len(edus)
    
    count_POE["less than high school"] = np.sum(edus == 1)/n
    count_POE["high school"] = np.sum(edus == 2)/n
    count_POE["more than high school but not college"] = np.sum(edus == 3)/n
    count_POE["college"] = np.sum(edus == 4)/n
    
    return count_POE
    raise NotImplementedError()
    
proportion_of_education()


# Question 2
def average_influenza_doses():
    import pandas as pd
    import numpy as np
    
     df = pd.read_csv("assets/NISPUF17.csv", index_col = 0)
        
    BREASTFEEDING_INFLUENZA = df[['CBF_01','P_NUMFLU']]

    BREASTFEEDING_INFLUENZA_1 = BREASTFEEDING_INFLUENZA[BREASTFEEDING_INFLUENZA['CBF_01'] == 1].dropna()
    BREASTFEEDING_INFLUENZA_2 = BREASTFEEDING_INFLUENZA[BREASTFEEDING_INFLUENZA['CBF_01'] == 2].dropna()

    FLU1 = BREASTFEEDING_INFLUENZA_1['P_NUMFLU']
    F1 = FLU1.sum() / FLU1.size

    FLU2 = BREASTFEEDING_INFLUENZA_2['P_NUMFLU']
    F2 = FLU2.sum() / FLU2.size

    print(F1, F2)
    return (F1, F2)
    raise NotImplementedError()

average_influenza_doses()


# Question 3
def chickenpox_by_sex():
    import pandas as pd
    import numpy as np
    
    df = pd.read_csv("assets/NISPUF17.csv", index_col = 0)
    CPOX_SEX = df[["SEX", "HAD_CPOX", "P_NUMVRC"]].dropna()
    CPOX_SEX = CPOX_SEX[CPOX_SEX["P_NUMVRC"] > 0]
    
    CPOX_SEX_M = CPOX_SEX[CPOX_SEX["SEX"] == 1]
    CPOX_SEX_F = CPOX_SEX[CPOX_SEX["SEX"] == 2]
    
    CPOX_F = CPOX_SEX_F[(CPOX_SEX_F["HAD_CPOX"] == 1) & (CPOX_SEX_F["P_NUMVRC"] >= 1)]
    NCPOX_F = CPOX_SEX_F[(CPOX_SEX_F["HAD_CPOX"] == 2) & (CPOX_SEX_F["P_NUMVRC"] >= 1)]
    
    RATIO_M = len(CPOX_SEX_M[CPOX_SEX_M["HAD_CPOX"] == 1])/len(CPOX_SEX_M[CPOX_SEX_M["HAD_CPOX"] == 2])
    RATIO_F = len(CPOX_SEX_F[CPOX_SEX_F["HAD_CPOX"] == 1])/len(CPOX_SEX_F[CPOX_SEX_F["HAD_CPOX"] == 2])
    
    return {"male": RATIO_M, "female": RATIO_F}
    raise NotImplementedError()

chickenpox_by_sex()


# Question 4
def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    df = pd.read_csv("assets/NISPUF17.csv")
    DOSES_HADCPOX = df[(df['P_NUMVRC'] >=0) & (df['HAD_CPOX'] <= 2)]
    
    CPOX_NO_YES = DOSES_HADCPOX['HAD_CPOX']
    NUM_DOSES = DOSES_HADCPOX['P_NUMVRC']
    
    # this is just an example dataframe
    df = pd.DataFrame({"had_chickenpox_column":CPOX_NO_YES,
                   "num_chickenpox_vaccine_column":NUM_DOSES})

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    
    # just return the correlation
    return corr
    raise NotImplementedError()

corr_chickenpox()    
