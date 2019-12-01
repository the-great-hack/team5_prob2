

import UIKit
import MapKit

class MapViewController: UIViewController {

    @IBOutlet weak var mapView: MKMapView!
    @IBOutlet weak var timePreferenceSwitch: UISwitch!
    @IBOutlet weak var costPreferenceSwitch: UISwitch!
    @IBOutlet weak var familySwitch: UISwitch!
    
    let locationManager = CLLocationManager()
    var locationUpdated = false
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
        if CLLocationManager.locationServicesEnabled()
        {
            let status: CLAuthorizationStatus = CLLocationManager.authorizationStatus()
            if status != CLAuthorizationStatus.authorizedWhenInUse
            {
                locationManager.requestWhenInUseAuthorization()
            }
        }
        mapView.delegate = self
    }
    
    @IBAction func actionChalo(_ sender: Any) {

        RideService(networkManager: NetworkManager()).getRidesBetween(point1: mapView.userLocation.coordinate, point2: mapView.userLocation.coordinate, completion: {(result) in
            switch result {
            case .success(let rides):
                guard let ctrl = self.storyboard?.instantiateViewController(withIdentifier: "ResultViewController") as? ResultViewController else {return}
                ctrl.mockData = rides
                self.present(ctrl, animated: true, completion: nil)
            default:
                break
            }
        })
    }
    
    func mapView(mapView: MKMapView, viewForAnnotation annotation: MKAnnotation) -> MKAnnotationView? {
        if annotation is MKUserLocation {
            return nil
        }

        let reuseId = "pin"
        var pinView = mapView.dequeueReusableAnnotationView(withIdentifier: reuseId) as? MKPinAnnotationView
        if pinView == nil {
            pinView = MKPinAnnotationView(annotation: annotation, reuseIdentifier: reuseId)
            pinView?.isDraggable = true
        }
        else {
            pinView?.annotation = annotation
        }

        return pinView
    }
    
    func addAnnotation(coordinates: CLLocationCoordinate2D) {
        mapView.removeAnnotations(mapView.annotations)
        let annotation = MKPointAnnotation()
        annotation.coordinate = mapView.centerCoordinate
        annotation.title = "Destination"
        annotation.subtitle = "Use chalo to get to here"
        mapView.addAnnotation(annotation)
    }
}

extension MapViewController: MKMapViewDelegate {
    
    func mapView(_ mapView: MKMapView, didUpdate userLocation: MKUserLocation) {
        guard !locationUpdated else {
            return
        }
        let viewRegion = MKCoordinateRegion(center: mapView.userLocation.coordinate, latitudinalMeters: 2000, longitudinalMeters: 2000)
        mapView.setRegion(viewRegion, animated: false)
        mapView.showsUserLocation = true
        addAnnotation(coordinates: mapView.userLocation.coordinate)
        locationUpdated = true
    }
    
    func mapView(_ mapView: MKMapView, regionDidChangeAnimated animated: Bool) {
        self.mapView.removeAnnotations(mapView.annotations)
        addAnnotation(coordinates: mapView.centerCoordinate)
    }
}

