import sys
import StrawEngine
sys.path.append(StrawEngine.__file__[::-1].split("/",1)[1][::-1])
from StrawEngine.straw import main as mainapi
main = lambda x: mainapi(x, True)