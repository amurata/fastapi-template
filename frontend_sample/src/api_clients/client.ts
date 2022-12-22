import { API_HOST } from 'config';
import {
  JobsApi,
  UsersApi,
} from './api';
import { Configuration } from './configuration';

const authConfig = new Configuration({
  basePath: API_HOST,
  baseOptions: { withCredentials: true },
});
const nonAuthConfig = new Configuration({
  basePath: API_HOST,
  baseOptions: { withCredentials: false },
});

export const UsersApiClient = new UsersApi(nonAuthConfig);
export const JobsApiClient = new JobsApi(nonAuthConfig);
