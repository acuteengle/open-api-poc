/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Create Pokemon
*
* pokemonCreateRequest PokemonCreateRequest 
* returns Pokemon
* */
const createPokemon = ({ pokemonCreateRequest }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        pokemonCreateRequest,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Delete Pokemon by ID
*
* pokemonId UUID Unique ID of a Pokemon.
* no response value expected for this operation
* */
const deletePokemonById = ({ pokemonId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        pokemonId,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Get Pokemon by ID
*
* pokemonId UUID Unique ID of a Pokemon.
* returns Pokemon
* */
const getPokemonById = ({ pokemonId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        pokemonId,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* List Pokemon
*
* limit Integer Maximum number of Pokemon to return. (optional)
* offset Integer Number of Pokemon to skip. (optional)
* returns PokemonListResponse
* */
const listPokemon = ({ limit, offset }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        limit,
        offset,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Replace Pokemon by ID
*
* pokemonId UUID Unique ID of a Pokemon.
* pokemonCreateRequest PokemonCreateRequest 
* returns Pokemon
* */
const replacePokemonById = ({ pokemonId, pokemonCreateRequest }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        pokemonId,
        pokemonCreateRequest,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Update Pokemon by ID
*
* pokemonId UUID Unique ID of a Pokemon.
* pokemonUpdateRequest PokemonUpdateRequest 
* returns Pokemon
* */
const updatePokemonById = ({ pokemonId, pokemonUpdateRequest }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        pokemonId,
        pokemonUpdateRequest,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);

module.exports = {
  createPokemon,
  deletePokemonById,
  getPokemonById,
  listPokemon,
  replacePokemonById,
  updatePokemonById,
};
