/**
 * The PokemonController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic routes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/PokemonService');
const createPokemon = async (request, response) => {
  await Controller.handleRequest(request, response, service.createPokemon);
};

const deletePokemonById = async (request, response) => {
  await Controller.handleRequest(request, response, service.deletePokemonById);
};

const getPokemonById = async (request, response) => {
  await Controller.handleRequest(request, response, service.getPokemonById);
};

const listPokemon = async (request, response) => {
  await Controller.handleRequest(request, response, service.listPokemon);
};

const replacePokemonById = async (request, response) => {
  await Controller.handleRequest(request, response, service.replacePokemonById);
};

const updatePokemonById = async (request, response) => {
  await Controller.handleRequest(request, response, service.updatePokemonById);
};


module.exports = {
  createPokemon,
  deletePokemonById,
  getPokemonById,
  listPokemon,
  replacePokemonById,
  updatePokemonById,
};
