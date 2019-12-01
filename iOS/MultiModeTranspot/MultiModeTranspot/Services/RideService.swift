

import Foundation
import MapKit

enum APIResult<T> {
    case success(T)
    case error(String)
}

protocol RideServiceProtocol {
    func getRidesBetween(point1: CLLocationCoordinate2D, point2: CLLocationCoordinate2D, completion: @escaping (APIResult<[RideModel]>)-> Void)
}

class RideService: RideServiceProtocol {
    
    private let networkManager: NetworkManagerProtocol
    
    init(networkManager: NetworkManagerProtocol) {
        self.networkManager = networkManager
    }
    
    func getRidesBetween(point1: CLLocationCoordinate2D, point2: CLLocationCoordinate2D, completion: @escaping (APIResult<[RideModel]>) -> Void) {
        let router = Routers.poiList(point1: point1, point2: point2)
        networkManager.requestObject(router) { (data: Data?, error: String?) in
            guard let data = data, let ridesModel = try? JSONDecoder().decode([RideModel].self, from: data) else {
                completion(APIResult.error(error ?? "Unknown error occured."))
                return
            }
            completion(APIResult.success(ridesModel))
        }
    }
}
