

import UIKit
import MapKit

class MapViewController: UIViewController {

    @IBOutlet weak var mapView: MKMapView!
    @IBOutlet weak var timePreferenceSwitch: UISwitch!
    @IBOutlet weak var costPreferenceSwitch: UISwitch!
    @IBOutlet weak var familySwitch: UISwitch!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    

    @IBAction func actionChalo(_ sender: Any) {
        guard let ctrl = storyboard?.instantiateViewController(identifier: "ResultViewController") else {return}
        present(ctrl, animated: true, completion: nil)
    }
    

}
