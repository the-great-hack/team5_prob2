
import Foundation

struct RideModel: Codable {
    var steps: [StepModel]
    var totalCost: String
    var arrivalTime: String
}
