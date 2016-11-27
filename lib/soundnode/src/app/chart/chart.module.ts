import { NgModule }      from '@angular/core';
import { CommonModule }  from '@angular/common';

import { ChartComponent }  from './chart.component';
import { routing }    from './chart.routing';

@NgModule({
  imports:      [ CommonModule, routing ],
  declarations: [ ChartComponent ],
  providers:    [  ]
})
export class ChartModule {}

