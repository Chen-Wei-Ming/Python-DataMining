
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils

data = MLUtils.loadLibSVMFile(sc, 'deaths_svm_will.txt')
(trainingData, testData) = data.randomSplit([0.75, 0.25])
model = DecisionTree.trainClassifier(trainingData, numClasses=2, categoricalFeaturesInfo={},impurity='gini', maxDepth=5, maxBins=32)
predictions = model.predict(testData.map(lambda x: x.features))
labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
accuracy= labelsAndPredictions.filter(lambda (v, p): v == p).count() / float(testData.count())
print('Accuracy = ' + str(accuracy))
TP = float(labelsAndPredictions.filter(lambda (v, p): v == p and p == 1 ).count())
TN = float(labelsAndPredictions.filter(lambda (v, p): v == p and p == 0 ).count())
FP = float(labelsAndPredictions.filter(lambda (v, p): v != p and p == 1 ).count())
FN = float(labelsAndPredictions.filter(lambda (v, p): v != p and p == 0 ).count())
datasum = float(TP+TN+FP+FN)
print('TP = ' + str(TP))
print('TN = ' + str(TN))
print('FP = ' + str(FP))
print('FN = ' + str(FN))
accuracyFormEvaluation = (TP + TN) / datasum
precisionFormEvaluation = TP / (TP + FP)
recallFormEvaluation = TP / (TP + FN)
print('AccuracyFormEvaluation = ' + str(accuracyFormEvaluation))
print('PrecisionFormEvaluation = ' + str(precisionFormEvaluation))
print('RecallFormEvaluation = ' + str(recallFormEvaluation))
print('Learned classification tree model:')
print(model.toDebugString())
# from pyspark.mllib.evaluation import MulticlassMetrics
# metrics = MulticlassMetrics(labelsAndPredictions)\
# metrics.precision()
# metrics.recall()
