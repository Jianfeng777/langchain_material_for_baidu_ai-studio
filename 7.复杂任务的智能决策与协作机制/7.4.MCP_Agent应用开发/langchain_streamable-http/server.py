from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DogUtils")  # 工具服务名称

@mcp.tool()
def calculate(what: str) -> str:
  """
  calculate:
  e.g. calculate: 4 * 7 / 3
  Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary
  """
  return str(eval(what))

@mcp.tool()
def average_dog_weight(name: str) -> str:
 """
 average_dog_weight:
 e.g. average_dog_weight: Collie
 returns average weight of a dog when given the breed
 """
 name = name.lower()
 if "scottish terrier" in name:
  return "Scottish Terriers average 20 lbs"
 elif "border collie" in name:
  return "A Border Collie's average weight is 37 lbs"
 elif "toy poodle" in name:
  return "A Toy Poodle's average weight is 7 lbs"
 else:
  return "An average dog weighs 50 lbs"

if __name__ == "__main__":
    mcp.run(transport="streamable-http") 