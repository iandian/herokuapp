import { ModuleWithProviders } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ChartComponent } from './chart.component';

export const routing: ModuleWithProviders = RouterModule.forChild([
  { path: '', component: ChartComponent }
]);
