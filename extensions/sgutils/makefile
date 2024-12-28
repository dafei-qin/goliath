export CUDA_VERSION:=$(nvcc --version | sed -n 's/^.*release \([0-9]\+\.[0-9]\+\).*$/\1/p')
# export CPATH:=/usr/local/cuda-${CUDA_VERSION}/targets/x86_64-linux/include:${CPATH}
export CPATH:=${CONDA_PREFIX}/include:${CPATH}
export LD_LIBRARY_PATH:=${CONDA_PREFIX}/lib:${LD_LIBRARY_PATH}
export PATH:=${CONDA_PREFIX}/bin:${PATH}
all:
	python setup.py build_ext --inplace
