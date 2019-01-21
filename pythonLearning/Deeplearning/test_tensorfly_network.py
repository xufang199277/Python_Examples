# test tensorfly_network.py
import minst_loader
import tensorfly_network
training_data, validation_data, test_data =minst_loader.load_data_wrapper()
net = tensorfly_network.Network([784,40,10])
net.SGD(training_data,30,20,4.0,test_data = test_data)