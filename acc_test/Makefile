
target := 10.63.246.13

all: regs mem basic mnist 

regs:
	python3 peripheral.py pa_regs.json $(target)
	python3 peripheral.py dma_regs.json $(target)
	python3 peripheral.py peri_regs.json $(target)
	
mem:
	python3 memtest.py memtest.json $(target)
	
basic:
	python3 pa_test.py test_cases.json $(target)

mnist:
	python3 pa_test.py mnist.json $(target)

clean:
	rm -rf __pycache__ *.pyc data/output*.dat data/mnist_output_*.dat
