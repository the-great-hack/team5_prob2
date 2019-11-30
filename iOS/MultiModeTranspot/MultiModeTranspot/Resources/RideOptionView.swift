//
//  RideOptionView.swift
//  MultiModeTranspot
//
//  Created by Shakeel Ahmad on 30/11/2019.
//  Copyright © 2019 Bashir Ahmad. All rights reserved.
//

import UIKit

class RideOptionView: UIView {

    @IBOutlet weak var separatorHeightConstraint: NSLayoutConstraint!
    @IBOutlet weak var locationLabel: UILabel!
    @IBOutlet weak var typeLabel: UILabel!
    
    var model: StepModel! {
        didSet {
            locationLabel.text = model.locationTitle
            typeLabel.text = model.vehicleType
        }
    }

    var isFirstCell: Bool! {
        didSet {
            separatorHeightConstraint.constant = isFirstCell ? 0 : 30
        }
    }
    
}
