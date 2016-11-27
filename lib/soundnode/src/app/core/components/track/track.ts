import { Component, EventEmitter, Input, Output, ChangeDetectionStrategy } from '@angular/core';
import { TrackResource } from '../../interfaces/track.resource.d';

@Component({
  selector: 'track',
  template: require('./track.html'),
  styleUrls: [ 'track.css' ],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class Track {
  @Input() data: TrackResource;

  showBigArtwork(img) {
      let newArtwork;
      if ( img === null ) {
          newArtwork = img.replace('large', 't300x300');
          return newArtwork;
      } else {
          newArtwork = 'public/img/song-placeholder.png';
          return newArtwork;
      }
  };

}
