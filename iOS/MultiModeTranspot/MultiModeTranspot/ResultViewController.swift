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
    var totalCost: Int
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

    @IBOutlet weak var stackview: UIStackView!
    
    let mockData = [
                    RideModel(steps: [
                            StepModel(locationTitle: "A", vehicleType: "Car"),
                            StepModel(locationTitle: "B", vehicleType: "Bus"),
                            StepModel(locationTitle: "C", vehicleType: "")
                            ],
                        totalCost: 450, arrivalTime: "12:50PM"),
                    
                    RideModel(steps: [
                        StepModel(locationTitle: "D", vehicleType: "Bike"),
                        StepModel(locationTitle: "E", vehicleType: "Bus"),
                        StepModel(locationTitle: "F", vehicleType: "Car"),
                        StepModel(locationTitle: "E", vehicleType: "")
                        ],
                    totalCost: 800, arrivalTime: "8:50 PM")
                ]
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        initGUI()
    }
    
    func initGUI() {
        for ride in mockData {
            for step in ride.steps {
                let optionView = UINib(nibName: "RideOptionView", bundle: Bundle.main).instantiate(withOwner: self, options: nil).first as! RideOptionView
                stackview.addArrangedSubview(optionView)
                //optionView.translatesAutoresizingMaskIntoConstraints = false
                optionView.heightAnchor.constraint(equalToConstant: 53).isActive = true
                optionView.model = step
                optionView.isFirstCell = ride.steps.firstIndex{$0 == step} == 0
            }
            
            let priceCellView = UINib(nibName: "PirceCellView", bundle: Bundle.main).instantiate(withOwner: self, options: nil).first as! PriceCellView
            stackview.addArrangedSubview(priceCellView)
            //priceCellView.translatesAutoresizingMaskIntoConstraints = false
            priceCellView.heightAnchor.constraint(equalToConstant: 72).isActive = true
            priceCellView.price = ride.totalCost
            priceCellView.time = ride.arrivalTime
            
            let view = UIView()
            stackview.addArrangedSubview(view)
            view.translatesAutoresizingMaskIntoConstraints = false
            view.heightAnchor.constraint(equalToConstant: 20).isActive = true
        }
    }
}
