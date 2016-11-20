import { Component, Input } from '@angular/core';

@Component({
  moduleId: module.id,
  selector: 'song-track',
  templateUrl: 'track.component.html',
  styleUrls: [ 'track.component.css' ],
})

export class TrackComponent {
  @Input() data: any;

  constructor() {}
}
