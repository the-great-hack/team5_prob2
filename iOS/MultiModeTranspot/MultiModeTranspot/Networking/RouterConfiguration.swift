
import Foundation

protocol RouterConfiguration {
    var method: String { get }
    var apiURL: URL { get }
    var baseUrl: String { get }
}

extension RouterConfiguration {
    var baseUrl: String {
        return "http://127.0.0.1:5000?"
    }
    var method: String { return "get" }
}

extension RouterConfiguration {
    public func asURLRequest() -> URLRequest {
        var urlRequest = URLRequest(url: apiURL)
        urlRequest.httpMethod = method
        return urlRequest
    }
}
