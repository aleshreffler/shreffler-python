TOOL NAME: Conduct Multi-Classification Accuracy Assessment Comparison

DESCRIPTION: This script simplifies the process of conducting an accuracy assessment on more than one landcover classification method. This accuracy assessment includes comparing classification results to ground truthed points and computing error matrices.It also reports the relevant statistics, including the overall accuracy (%) of each classification and identifies the most inaccurate classes. Finally, a layer of misclassified points is produced which can be used to verify accurate ground truthing and classification results.

REQUIREMENTS: Prior to running this script, the user should have already run the Create Accuracy Assessment Points geoprocessing tool and updated the 'GrndTruth' field with ground truthed information. This script also requires that assessment classifications be located in a single file geodatabase with the first five characters being unique in each file name. Finally, given that this tool assumes that a comparison is being made between like classes, the classes for each classification (and the ground truthed points) must be standardized using numerical values.

** ALSO REQUIRES THE PIP INSTALLATION OF THE FOLLOWING TWO MODULES: **
	~ pip install pandas_ml
	~ pip install XlsxWriter

USAGE: This script should be used in instances where there exists multiple classification results which need to be evaluated using an accuracy assessment. This tool differs from the traditional accuracy assessment workflow by removing the need to ground truth multiple times before computing each confusion matrix individually. Consider a user which has collected a classification result from each member of a group. In order to determine which member had the most accurate classification, the user would only need to run this tool once provided each of the script tool requirements are satisfied. This simplifies and accelerates the accuracy assessment process, providing users with more time to accomplish other project management tasks. 


Ground Truth Points:
This parameter must be a point feature class produced by the Create Accuracy Assessment Points tool. In order to retain original, intact data, a copy is made of this layer during the analysis. The "Classified' field will have no impact on the results of this tool as it will be deleted once a copy is made. The geodatabase location of this feature class will be shared with the copy, which eventually becomes the Assessment and Inaccuraccy point files. 

Classification Geodatabase:
This parameter must be a geodatabase containing only the classifications to be assessed. They can be of either the feature class or raster type. This script is not written so that it will process Feature Datasets within the geodatabase. The first 5 characters will need to be unique in each classification in order to avoid errors. The numerical class values for each classification should match the ground truth points. If there are additional classes which are not present in the ground truth data, there may be skewed results. 

Point Geodatabase Location:
This parameter describes the output folder location for the geodatabase which will contain the classification point feature classes. A geodatabase will be created in the folder provided.
