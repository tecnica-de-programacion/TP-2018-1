//class Dog {
//    var name: String
//    var breed: String
//    
//    init(name: String, breed: String) {
//        self.name = name
//        self.breed = breed
//    }
//    
//    func run () {
//        print(self.name, "is runing")
//    }
//    
//    func bark () {
//        print("guarf!")
//    }
//}
//
//
//let luky = Dog(name: "luky", breed:"Chihuahua")
//luky.run()
//luky.bark()

// ********************************************

//class Dog {
//    static var sound = "guau!"
//    
//    var sound = "guarf!"
//    var name: String
//    var breed: String
//
//    init(name: String, breed: String) {
//        self.name = name
//        self.breed = breed
//    }
//
//    func run () {
//        print(self.name, "is runing")
//    }
//
//    func bark () {
//        print(self.sound)
//        print(Dog.sound)
//    }
//}
//
//
//let luky = Dog(name: "luky", breed:"Chihuahua")
//luky.run()
//luky.bark()
//
//luky.sound = "otro"
//Dog.sound = "otro2"
//luky.bark()

// ********************************************

//class Dog {
//    static var generalTag =  0
//    
//    var sound = "guarf!"
//    var name: String
//    var breed: String
//    var tag: Int
//    var info: String
//    
//    init(name: String, breed: String) {
//        self.name = name
//        self.breed = breed
//        tag = Dog.generalTag
//        self.info = "Name: \(self.name), Breed: \(self.breed), Tag: \(self.tag)"
//        Dog.generalTag += 1
//    }
//    
//    static func count() {
//        print("Number of dogs: \(generalTag)")
//    }
//}
//
//class DogsCataloger {
//    static func catalog(form dogs: [Dog]) -> [String : Int] {
//        var catalog : [String : Int] = [:]
//        for dog in dogs {
//            if catalog[dog.breed] != nil {
//                catalog[dog.breed]? += 1
//            } else {
//                catalog[dog.breed] = 1
//            }
//        }
//        return catalog
//    }
//}
//
//
//let luky = Dog(name: "luky", breed:"Chihuahua")
//print(luky.info)
//
//let spike = Dog(name: "luspikeky", breed:"Golden")
//print(spike.info)
//
//Dog.count()
//
//let dogs = [luky, spike]
//print(DogsCataloger.catalog(form: dogs))


// ********************************************

class Employe {
    
    var firstName: String
    var lastName: String
    var fullName: String {
        set {
            let splitName = fullName.components(separatedBy: " ")
            firstName = splitName.first!
            lastName = splitName.last!
        }
        
        get {
            return "\(firstName) \(lastName)"
        }
    }
    
    init (firstName: String, lastName: String) {
        self.firstName = firstName
        self.lastName = lastName
    }
}


let emp_1 = Employe(firstName: "Lalo", lastName: "Landa")
emp_1.fullName

emp_1.firstName = "Eduardo"
emp_1.fullName

emp_1.fullName = "Lalo Landa"
emp_1.firstName
emp_1.fullName

print(emp_1)


// ********************************************
//class Dog {
//    static var generalTag =  0
//
//    var name: String
//    var breed: String
//    var tag: Int
//
//    init(name: String, breed: String) {
//        self.name = name
//        self.breed = breed
//        tag = Dog.generalTag
//        Dog.generalTag += 1
//    }
//
//    static func count() {
//        print("Number of dogs: \(generalTag)")
//    }
//}
//
////extension Dog: CustomStringConvertible {
////    var description: String {
////        return "Name: \(self.name), Breed: \(self.breed), Tag: \(self.tag)"
////    }
////}
//
//let luky = Dog(name: "luky", breed:"Chihuahua")
//print(luky)

// ********************************************

//class Dog {
//    static var generalTag =  0
//
//    var name: String
//    var breed: String
//    var tag: Int
//
//    init(name: String, breed: String) {
//        self.name = name
//        self.breed = breed
//        tag = Dog.generalTag
//        Dog.generalTag += 1
//    }
//}
//
//extension Dog {
//    static func +(left: Dog, right: Dog) -> [Dog] {
//        return [left, right]
//    }
//}
//
//extension Dog: CustomStringConvertible {
//    var description: String {
//        return "Name: \(self.name), Breed: \(self.breed), Tag: \(self.tag)"
//    }
//}
//
//let luky = Dog(name: "luky", breed:"Chihuahua")
//let pedro = Dog(name: "lupedroky", breed:"Chihuahua")
//print(luky + pedro)
