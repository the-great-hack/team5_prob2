//
//  ResultViewController.swift
//  MultiModeTranspot
//
//  Created by Shakeel Ahmad on 30/11/2019.
//  Copyright © 2019 Bashir Ahmad. All rights reserved.
//

import UIKit
struct RideModel {
    var steps: [StepModel]
    var totalCost: String
    var arrivalTime: String
}

struct StepModel {
    var locationTitle: String
    var vehicleType: String
}

func ==(_ lhs: StepModel, _ rhs: StepModel) -> Bool {
    return lhs.locationTitle == rhs.locationTitle && lhs.vehicleType == rhs.vehicleType
}

class ResultViewController: UIViewController {

    @IBOutlet weak var tableview: UITableView!
    
    
    let mockData = [
                    RideModel(steps: [
                            StepModel(locationTitle: "A", vehicleType: "Car"),
                            StepModel(locationTitle: "B", vehicleType: "Bus"),
                            StepModel(locationTitle: "C", vehicleType: "Completed")
                            ],
                        totalCost: "450", arrivalTime: "12:50PM"),
                    
                    RideModel(steps: [
                        StepModel(locationTitle: "D", vehicleType: "Bike"),
                        StepModel(locationTitle: "E", vehicleType: "Bus"),
                        StepModel(locationTitle: "F", vehicleType: "Car"),
                        StepModel(locationTitle: "E", vehicleType: "Completed")
                        ],
                    totalCost: "800", arrivalTime: "8:50 PM")
                ]
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    func initGUI(stackview: UIStackView, ride: RideModel) {
        for v in stackview.subviews {
            v.removeFromSuperview()
            stackview.removeArrangedSubview(v)
        }
        addSpacer(stackview: stackview)
        var isFirstCell = true
        for step in ride.steps {
            let optionView = UINib(nibName: "RideOptionView", bundle: Bundle.main).instantiate(withOwner: self, options: nil).first as! RideOptionView
            stackview.addArrangedSubview(optionView)
            optionView.model = step
            optionView.isFirstCell = isFirstCell
            isFirstCell = false
        }
        let priceCellView = UINib(nibName: "PirceCellView", bundle: Bundle.main).instantiate(withOwner: self, options: nil).first as! PriceCellView
        stackview.addArrangedSubview(priceCellView)
        priceCellView.price = ride.totalCost
        priceCellView.time = ride.arrivalTime
        addSpacer(stackview: stackview)
    }
    
    func addSpacer(stackview: UIStackView) {
        let view = UIView()
        stackview.addArrangedSubview(view)
        view.translatesAutoresizingMaskIntoConstraints = false
        view.heightAnchor.constraint(equalToConstant: 10).isActive = true
    }
}


extension ResultViewController: UITableViewDelegate, UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return mockData.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        let stackview = cell.contentView.viewWithTag(1) as! UIStackView
        initGUI(stackview: stackview, ride: mockData[indexPath.row])
        return cell
    }
}
