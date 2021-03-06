import { Injectable, Optional } from '@angular/core';

const SOUNDCLOUD_API_V2 = 'https://api-v2.soundcloud.com/';
let nextPageUrl = '';


@Injectable()
export class UserService {
  id = nextId++;
  private _userName = 'Sherlock Holmes';

  constructor(@Optional() config: UserServiceConfig) {
    if (config) { this._userName = config.userName; }
  }

  get userName() {
    // Demo: add a suffix if this service has been created more than once
    const suffix = this.id > 1 ? ` times ${this.id}` : '';
    return this._userName + suffix;
  }
}



import { Http, URLSearchParams, Response, RequestOptionsArgs, Headers } from '@angular/http';
import { Injectable } from '@angular/core';
import { window } from '@angular/platform-browser/src/facade/browser';
import { YOUTUBE_API_KEY, CLIENT_ID } from './constants';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/toPromise';
import 'rxjs/add/observable/fromPromise';

interface YoutubeApiServiceOptions {
  url?: string;
  http?: Http;
  idKey?: string;
  config?: any;
}

export class YoutubeApiService {
  url: string;
  http: Http;
  idKey: string;
  isSearching: Boolean = false;
  items: Array<any> = [];
  config: URLSearchParams = new URLSearchParams();
  nextPageToken: string;
  private accessToken: string;

  constructor(options: YoutubeApiServiceOptions | any) {
      this.resetConfig();
      if (options) {
          this.url = options.url;
          this.http = options.http;
          this.idKey = options.idKey || '';
          if (options.config) {
              this.setConfig(options.config);
          }
      }
  }

  setConfig(config) {
      Object.keys(config).forEach(option => {
          this.config.set(option, config[option]);
      });
  }

  setToken(token: string) {
      this.accessToken = token;
  }

  hasToken (): boolean {
      return this.accessToken.length > 0;
  }

  resetConfig() {
      this.config.set('part', 'snippet,contentDetails');
      this.config.set('key', YOUTUBE_API_KEY);
      this.config.set('maxResults', '50');
      this.config.set('pageToken', '');
  }
  getList() {
      const accessToken = this.accessToken;
      this.isSearching = true;
      let options: RequestOptionsArgs = {
          search: this.config,
          headers: this.createHeaders()
      };
      return this.http.get(this.url, options)
          .map(response => response.json());
  }

  list(id) {
    if (this.idKey) {
        this.config.set(this.idKey, id);
    }

    this.isSearching = true;
    let options: RequestOptionsArgs = {
        search: this.config,
        headers: this.createHeaders()
    };
    return this.http.get(this.url, options)
      .toPromise()
      .then(response => response.json())
      .then(response => {
          this.nextPageToken = response.nextPageToken;
          this.isSearching = false;
          return response;
      });
  }

  searchMore() {
    if (!this.isSearching && this.items.length) {
      this.config.set('pageToken', this.nextPageToken);
    }
  }

  resetPageToken () {
    this.config.set('pageToken', '');
  }

  createHeaders () {
    const accessToken = this.accessToken;
    const headersOptions = {};
    if (accessToken) {
      headersOptions['authorization'] = `Bearer ${accessToken}`;
    }
    return new Headers(headersOptions);
  }
}
