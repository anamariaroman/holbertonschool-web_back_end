import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const obj = {};
  try {
    const user = await createUser();
    const photo = await uploadPhoto();
    Object.assign(obj, {
      photo,
      user,
    });
  } catch (err) {
    Object.assign(obj, {
      photo: null,
      user: null,
    });
  }
  return obj;
}
