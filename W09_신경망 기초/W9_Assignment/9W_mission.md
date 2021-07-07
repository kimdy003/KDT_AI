# 9Week - 신경망 실습 과제

## 1. multilayer perceptron 이해
data는 MNIST 사용  
batch_size : 20,  
Epoch : 10  
activate function : ReLu 사용
Loss Function : CrossEntropyLoss()  
Optimizer : SGD  
Network architecture (  
&nbsp;&nbsp;&nbsp;&nbsp;(fc1) Linear(in_features=784, out_featrues = 512, bias=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(fc2) Linear(in_features=512, out_featrues = 10, bias=True)  
)

### Test Accuracy : 91%

<br><hr>

## 2. 성능 향상 방법을 제안, 결과 확인
Epoch : 늘릴수 있지만, 늘리면 수행시간이 늘어나므로 일단 제외  

> 현재 Network는 fully connected 계층 2개로만 이뤄져있다.(input - output)  
따라서 중간에 hidden layer를 추가하고, 중간에 Batch Normalization를 넣어줌으로써 성능 향상을 바래본다.  
(input - layer - bn(layer) - bn(layer) - bn(layer) - layer - output)

Network architecture (  
&nbsp;&nbsp;&nbsp;&nbsp;(layer0): Linear(in_features=784, out_features=512, bias=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(layer1): Linear(in_features=512, out_features=256, bias=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(layer2): Linear(in_features=256, out_features=128, bias=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(layer3): Linear(in_features=128, out_features=64, bias=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(layer4): Linear(in_features=64, out_features=32, bias=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(layer5): Linear(in_features=32, out_features=16, bias=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(layer6): Linear(in_features=16, out_features=10, bias=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(bn0): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(bn1): BatchNorm1d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(bn2): BatchNorm1d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)  
&nbsp;&nbsp;&nbsp;&nbsp;(act): ReLU()  
)

### Test Accuracy : 98% 

<br><hr>

## 3. GPU 실행
to.device를 사용하여 GPU를 사용
``` python
# 아래 코드를 통해 현재 GPU를 사용하는지 확인
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# GPU 사용중이면, model를 GPU에 올려준다.
model = Net()
model.to(device)

...

# training 할 때, GPU에서 계산을 진행하기 위해
# data, target의 데이터들도 GPU에 올려 계산을 진행한다.
data, target = data.to(device), target.to(device)

...

# testing 할 때도 마찬가지로 data, target을 GPU에 올려주어 계산을 진행한다.
data, target = data.to(device), target.to(device)

...

```
### Test Accuracy : 97% 

<br>



