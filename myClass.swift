import Foundation

class myClass{
    func Main()
    {
        var str = "Hall� ";
        str.AddDaniel()
        print(str);
    }
}

extension String{
    mutating func AddDaniel()
    {
        self = self + "Daniel";
    }
}

let c = myClass();

c.Main();