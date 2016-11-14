// src/app/routes.ts
import {Home} from './components/home';     // ./components/home/index.ts

export default [
    {path: '/', component: Home, name: 'Home'},
    {path: 'charts', loadChildren: 'app/chart/chart.module#ChartModule'},
	{path: 'favorites', loadChildren: 'app/favorite/favorite.module#FavoriteModule'},
	{path: 'playlists', loadChildren: 'app/playlist/playlist.module#PlaylistModule'},
	{path: 'stream', loadChildren: 'app/stream/stream.module#StreamModule'},
	{path: 'tracks', loadChildren: 'app/track/track.module#TrackModule'}
];
