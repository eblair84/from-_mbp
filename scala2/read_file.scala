import scala.io.Source

object Main {
  def main(args: Array[String]){
  val filename = "awesome.txt"
  for (line <- Source.fromFile(filename).getLines) {
    println(line)
  }
  }
}
