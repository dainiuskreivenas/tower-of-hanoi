mkdir -p tests/results

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
export PYTHONPATH="${PYTHONPATH};:${SCRIPT_DIR}/rbs"

python3 -m tests.ToH_3 > ./tests/results/TowerOfHanoi_3.sp

python3 -m tests.ToH_4 > ./tests/results/TowerOfHanoi_4.sp

python3 -m tests.ToH_5 > ./tests/results/TowerOfHanoi_5.sp
