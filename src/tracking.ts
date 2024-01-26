import mixpanel from 'mixpanel-browser';

mixpanel.init('28371becc02343d0e56b33253c857292', {debug: true, track_pageview: true, persistence: 'localStorage'});
mixpanel.identify(mixpanel.get_distinct_id());
export const tracking = mixpanel