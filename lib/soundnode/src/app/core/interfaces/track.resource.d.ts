export interface TrackResource {
  id: string;
  stream_url: string;
  artwork_url: string;
  title: string;
  comment_count: string;
  likes_count: string;
  favoritings_count: string;
  reposts_count: string;
  user_favorite: string;
  user_reposted: string;
  user: {
    id: string;
    username: string;
    title: string;
    description: string;
    thumbnails: Object;
    channelTitle: string;
    categoryId: string;
    liveBroadcastContent: string;
    localized: Object;
  };
  contentDetails: any;
  statistics: any;
}
