//
//  PriceCellView.swift
//  MultiModeTranspot
//
//  Created by Shakeel Ahmad on 30/11/2019.
//  Copyright © 2019 Bashir Ahmad. All rights reserved.
//

import UIKit

class PriceCellView: UIView {
    
    @IBOutlet weak var priceLabel: UILabel!
    @IBOutlet weak var timeLabel: UILabel!
    
    var price: Int! {
        didSet {
            priceLabel.text = "\(String(describing: price))"
        }
    }
    
    var time: String! {
        didSet {
            timeLabel.text = time
        }
    }

}
