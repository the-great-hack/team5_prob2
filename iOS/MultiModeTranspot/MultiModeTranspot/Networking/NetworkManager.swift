
import Foundation

protocol NetworkManagerProtocol {
    func requestObject(_ router: RouterConfiguration, completion: @escaping ((Data?, String?) -> Void))
}
struct NetworkManager: NetworkManagerProtocol {
    func requestObject(_ router: RouterConfiguration, completion: @escaping ((Data?, String?) -> Void)) {
        let session = URLSession(configuration: URLSessionConfiguration.default)
        session.dataTask(with: router.asURLRequest()) { (data, response, error) in
            guard let data = data else {
                completion(nil, error?.localizedDescription)
                return
            }
            completion(data, nil)
        }.resume()
    }
}
