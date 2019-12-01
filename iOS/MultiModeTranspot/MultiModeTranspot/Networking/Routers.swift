
import Foundation
import MapKit

enum Routers: RouterConfiguration {
    case rides(point1: CLLocationCoordinate2D, point2: CLLocationCoordinate2D)
    var apiURL: URL {
        switch self {
        case .rides(let point1, let point2):
            return URL(string: baseUrl + "sLon=\(point1.longitude)&sLat=\(point1.latitude)&dLon=\(point2.longitude)&dLat=\(point2.latitude)")!
        }
    }
}
